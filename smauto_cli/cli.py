import sys
import click

from smauto.interpreter import interpret_model_from_path
from smauto.generator import generate_automation_graph_from_file


@click.group()
@click.pass_context
def cli(ctx):
    ctx.ensure_object(dict)


@cli.command(help='Interpreter')
@click.pass_context
@click.argument('model_path')
def interpret(ctx, model_path):
    interpret_model_from_path(model_path)


@cli.command(help='Automation Graph generator')
@click.pass_context
@click.argument('model_path')
def gen_automation_graph(ctx, model_path):
    generate_automation_graph_from_file(model_path)


def main():
    cli(obj={})
