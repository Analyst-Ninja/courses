import asyncio
from crawl4ai import AsyncWebCrawler


def main():

    async def main():
        async with AsyncWebCrawler() as crawler:
            result = await crawler.arun(
                url="https://pydantic.dev/docs/ai/overview/",
            )

            with open("data.md", "+a") as file:
                file.write(result.markdown)

    if __name__ == "__main__":
        asyncio.run(main())


if __name__ == "__main__":
    main()
