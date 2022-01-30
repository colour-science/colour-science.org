"""
Invoke - Tasks
==============
"""

from __future__ import annotations

from invoke import Context, task

__author__ = "Colour Developers"
__copyright__ = "Copyright (C) 2013-2021 - Colour Developers"
__license__ = "New BSD License - https://opensource.org/licenses/BSD-3-Clause"
__maintainer__ = "Colour Developers"
__email__ = "colour-developers@colour-science.org"
__status__ = "Production"

__all__ = ["upgrade", "formatting", "quality", "build"]


def _patch_invoke_annotations_support():
    """
    See https://github.com/pyinvoke/invoke/issues/357
    """

    import invoke
    from unittest.mock import patch
    from inspect import getfullargspec, ArgSpec

    def patched_inspect_getargspec(function):
        spec = getfullargspec(function)
        return ArgSpec(*spec[0:4])

    org_task_argspec = invoke.tasks.Task.argspec

    def patched_task_argspec(*args, **kwargs):
        with patch(
            target="inspect.getargspec", new=patched_inspect_getargspec
        ):
            return org_task_argspec(*args, **kwargs)

    invoke.tasks.Task.argspec = patched_task_argspec


_patch_invoke_annotations_support()


@task
def upgrade(
    ctx: Context,
    pyupgrade: bool = True,
    flynt: bool = True,
):
    """
    Upgrade the codebase with *pyupgrade* and *flynt*.

    Parameters
    ----------
    ctx
        Context.
    pyupgrade
        Whether to upgrade the codebase with *pyupgrade*.
    flynt
        Whether to upgrade the codebase with *flynt*.
    """

    if pyupgrade:
        print('Upgrading codebase with "pyupgrade"...')
        ctx.run("pre-commit run pyupgrade --all-files")

    if flynt:
        print('Upgrading codebase with "flynt"...')
        ctx.run("flynt .")


@task
def formatting(
    ctx: Context,
    black: bool = True,
):
    """
    Formats the codebase with *Black*.

    Parameters
    ----------
    ctx
        Context.
    black
        Whether to format the codebase with *Black*.
    """

    if black:
        print('Formatting codebase with "Black"...')
        ctx.run("black .")


@task
def quality(ctx, flake8: bool = True):
    """
    Checks the codebase with *Flake8* and lints various *restructuredText*
    files with *rst-lint*.

    Parameters
    ----------
    ctx
        Context.
    flake8
        Whether to check the codebase with *Flake8*.
    """

    if flake8:
        print('Checking codebase with "Flake8"...')
        ctx.run("flake8 .")


@task(upgrade, formatting, quality)
def build(ctx):
    """
    Builds the project.

    Parameters
    ----------
    ctx : invoke.context.Context
        Context.
    """

    print("Building...")
    ctx.run("nikola build")
