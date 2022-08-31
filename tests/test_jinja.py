from __future__ import annotations

import sys

from jinja2 import DictLoader, Environment

from heroicons.jinja import heroicon_outline, heroicon_solid, heroicon_mini


def make_environment(index_template: str) -> Environment:
    env = Environment(loader=DictLoader({"index": index_template}))
    env.globals.update(
        {
            "heroicon_outline": heroicon_outline,
            "heroicon_solid": heroicon_solid,
            "heroicon_mini": heroicon_mini,
        }
    )
    return env


def test_success_outline_simple():
    env = make_environment('{{ heroicon_outline("academic-cap") }}')
    template = env.get_template("index")

    result = template.render()

    expected_py37 = (
        '<svg aria-hidden="true" fill="none" height="24" '
        + 'stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"'
        + ' width="24">\n'
        + '  <path d="M12 14l9-5-9-5-9 5 9 5z" />\n'
        + '  <path d="M12 14l6.16-3.422a12.083 12.083 0 01.665 6.479A11.952 11.952 0 '
        + "0012 20.055a11.952 11.952 0 00-6.824-2.998 12.078 12.078 0 01.665-6.479L12 "
        + '14z" />\n'
        + '  <path d="M12 14l9-5-9-5-9 5 9 5zm0 0l6.16-3.422a12.083 12.083 0 01.665 '
        + "6.479A11.952 11.952 0 0012 20.055a11.952 11.952 0 00-6.824-2.998 12.078 "
        + '12.078 0 01.665-6.479L12 14zm-4 6v-7.5l4-2.222" stroke-linecap="round" '
        + 'stroke-linejoin="round" />\n'
        + "</svg>"
    )
    expected_py38plus = (
        '<svg fill="none" viewBox="0 0 24 24" '
        + 'stroke-width="2" stroke="currentColor" aria-hidden="true"'
        + ' width="24" height="24">\n'
        + '  <path d="M12 14l9-5-9-5-9 5 9 5z" />\n'
        + '  <path d="M12 14l6.16-3.422a12.083 12.083 0 01.665 6.479A11.952 11.952 0 '
        + "0012 20.055a11.952 11.952 0 00-6.824-2.998 12.078 12.078 0 01.665-6.479L12 "
        + '14z" />\n'
        + '  <path stroke-linecap="round" stroke-linejoin="round" '
        + 'd="M12 14l9-5-9-5-9 5 9 5zm0 0l6.16-3.422a12.083 12.083 0 01.665 '
        + "6.479A11.952 11.952 0 0012 20.055a11.952 11.952 0 00-6.824-2.998 12.078 "
        + '12.078 0 01.665-6.479L12 14zm-4 6v-7.5l4-2.222" />\n'
        + "</svg>"
    )
    if sys.version_info < (3, 8):
        expected = expected_py37
    else:
        expected = expected_py38plus
    assert result == expected


def test_success_outline_changed_path_attr():
    env = make_environment(
        '{{ heroicon_outline("academic-cap", stroke_linecap="butt") }}'
    )
    template = env.get_template("index")

    result = template.render()

    expected_py37 = (
        '<svg aria-hidden="true" fill="none" height="24" stroke="currentColor" '
        + 'stroke-width="2" viewBox="0 0 24 24" width="24">\n'
        + '  <path d="M12 14l9-5-9-5-9 5 9 5z" stroke-linecap="butt" />\n'
        + '  <path d="M12 14l6.16-3.422a12.083 12.083 0 01.665 6.479A11.952 11.952 0 '
        + "0012 20.055a11.952 11.952 0 00-6.824-2.998 12.078 12.078 0 01.665-6.479L12 "
        + '14z" stroke-linecap="butt" />\n'
        + '  <path d="M12 14l9-5-9-5-9 5 9 5zm0 0l6.16-3.422a12.083 12.083 0 01.665 '
        + "6.479A11.952 11.952 0 0012 20.055a11.952 11.952 0 00-6.824-2.998 12.078 "
        + '12.078 0 01.665-6.479L12 14zm-4 6v-7.5l4-2.222" stroke-linecap="butt" '
        + 'stroke-linejoin="round" />\n'
        + "</svg>"
    )
    expected_py38plus = (
        '<svg fill="none" viewBox="0 0 24 24" '
        + 'stroke-width="2" stroke="currentColor" aria-hidden="true" '
        + 'width="24" height="24">\n'
        + '  <path d="M12 14l9-5-9-5-9 5 9 5z" stroke-linecap="butt" />\n'
        + '  <path d="M12 14l6.16-3.422a12.083 12.083 0 01.665 6.479A11.952 11.952 0 '
        + "0012 20.055a11.952 11.952 0 00-6.824-2.998 12.078 12.078 0 01.665-6.479L12 "
        + '14z" stroke-linecap="butt" />\n'
        + '  <path stroke-linecap="butt" stroke-linejoin="round" '
        + 'd="M12 14l9-5-9-5-9 5 9 5zm0 0l6.16-3.422a12.083 12.083 0 01.665 '
        + "6.479A11.952 11.952 0 0012 20.055a11.952 11.952 0 00-6.824-2.998 12.078 "
        + '12.078 0 01.665-6.479L12 14zm-4 6v-7.5l4-2.222" />\n'
        + "</svg>"
    )
    if sys.version_info < (3, 8):
        expected = expected_py37
    else:
        expected = expected_py38plus
    assert result == expected


def test_success_outline_complete():
    env = make_environment(
        '{{ heroicon_outline("academic-cap", size=48, class="h-4 w-4", '
        + 'data_test="a < 2") }}'
    )
    template = env.get_template("index")

    result = str(template.render())

    expected_py37 = (
        '<svg aria-hidden="true" class="h-4 w-4" data-test="a &lt; 2" '
        + 'fill="none" height="48" stroke="currentColor" stroke-width="2" '
        + 'viewBox="0 0 24 24" width="48">\n'
        + '  <path d="M12 14l9-5-9-5-9 5 9 5z" />\n'
        + '  <path d="M12 14l6.16-3.422a12.083 12.083 0 01.665 6.479A11.952 11.952 0 '
        + "0012 20.055a11.952 11.952 0 00-6.824-2.998 12.078 12.078 0 01.665-6.479L12 "
        + '14z" />\n'
        + '  <path d="M12 14l9-5-9-5-9 5 9 5zm0 0l6.16-3.422a12.083 12.083 0 01.665 '
        + "6.479A11.952 11.952 0 0012 20.055a11.952 11.952 0 00-6.824-2.998 12.078 "
        + '12.078 0 01.665-6.479L12 14zm-4 6v-7.5l4-2.222" stroke-linecap="round" '
        + 'stroke-linejoin="round" />\n'
        + "</svg>"
    )
    expected_py38plus = (
        '<svg fill="none" viewBox="0 0 24 24" '
        + 'stroke-width="2" stroke="currentColor" aria-hidden="true" '
        + 'width="48" height="48" class="h-4 w-4" data-test="a '
        + '&lt; 2">\n'
        + '  <path d="M12 14l9-5-9-5-9 5 9 5z" />\n'
        + '  <path d="M12 14l6.16-3.422a12.083 12.083 0 01.665 6.479A11.952 11.952 0 '
        + "0012 20.055a11.952 11.952 0 00-6.824-2.998 12.078 12.078 0 01.665-6.479L12 "
        + '14z" />\n'
        + '  <path stroke-linecap="round" stroke-linejoin="round" '
        + 'd="M12 14l9-5-9-5-9 5 9 5zm0 0l6.16-3.422a12.083 12.083 0 01.665 '
        + "6.479A11.952 11.952 0 0012 20.055a11.952 11.952 0 00-6.824-2.998 12.078 "
        + '12.078 0 01.665-6.479L12 14zm-4 6v-7.5l4-2.222" />\n'
        + "</svg>"
    )
    if sys.version_info < (3, 8):
        expected = expected_py37
    else:
        expected = expected_py38plus
    assert result == expected


def test_success_solid():
    env = make_environment(
        '{{ heroicon_solid("academic-cap", size=40, class="h-4 w-4 inline") }}'
    )
    template = env.get_template("index")

    result = template.render()

    expected_py37 = (
        '<svg aria-hidden="true" class="h-4 w-4 inline" '
        + 'fill="currentColor" height="40" viewBox="0 0 20 20" width="40">\n'
        + '  <path d="M10.394 2.08a1 1 0 00-.788 0l-7 3a1 1 0 000 1.84L5.25 '
        + "8.051a.999.999 0 01.356-.257l4-1.714a1 1 0 11.788 1.838L7.667 "
        + "9.088l1.94.831a1 1 0 00.787 0l7-3a1 1 0 000-1.838l-7-3zM3.31 9.397L5 "
        + "10.12v4.102a8.969 8.969 0 00-1.05-.174 1 1 0 01-.89-.89 11.115 11.115 0 "
        + "01.25-3.762zM9.3 16.573A9.026 9.026 0 007 14.935v-3.957l1.818.78a3 3 0 "
        + "002.364 0l5.508-2.361a11.026 11.026 0 01.25 3.762 1 1 0 01-.89.89 8.968 "
        + "8.968 0 00-5.35 2.524 1 1 0 01-1.4 0zM6 18a1 1 0 001-1v-2.065a8.935 8.935 0 "
        + '00-2-.712V17a1 1 0 001 1z" />\n'
        + "</svg>"
    )
    expected_py38plus = (
        '<svg viewBox="0 0 20 20" '
        + 'fill="currentColor" aria-hidden="true" '
        + 'width="40" height="40" class="h-4 w-4 inline">\n'
        + '  <path d="M10.394 2.08a1 1 0 00-.788 0l-7 3a1 1 0 000 1.84L5.25 '
        + "8.051a.999.999 0 01.356-.257l4-1.714a1 1 0 11.788 1.838L7.667 "
        + "9.088l1.94.831a1 1 0 00.787 0l7-3a1 1 0 000-1.838l-7-3zM3.31 9.397L5 "
        + "10.12v4.102a8.969 8.969 0 00-1.05-.174 1 1 0 01-.89-.89 11.115 11.115 0 "
        + "01.25-3.762zM9.3 16.573A9.026 9.026 0 007 14.935v-3.957l1.818.78a3 3 0 "
        + "002.364 0l5.508-2.361a11.026 11.026 0 01.25 3.762 1 1 0 01-.89.89 8.968 "
        + "8.968 0 00-5.35 2.524 1 1 0 01-1.4 0zM6 18a1 1 0 001-1v-2.065a8.935 8.935 0 "
        + '00-2-.712V17a1 1 0 001 1z" />\n'
        + "</svg>"
    )
    if sys.version_info < (3, 8):
        expected = expected_py37
    else:
        expected = expected_py38plus
    assert result == expected
