import logging
import click

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s] %(levelname)-8s %(name)s: %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)

logger = logging.getLogger(__name__)


@click.command()
@click.argument("urls", nargs=-1)
@click.option(
    "--timeout",
    default=5,
    help="Timeout in seconds for each request.",
)
@click.option(
    "--verbose", "-v", is_flag=True, help="Enable debug logging."
)
def main(urls, timeout, verbose):
    logger.info(f"Received urls: {urls}")
    logger.info(f"Received timeout: {timeout}")
    logger.info(f"Received verbose: {verbose}")
