import asyncio

async def fetch_data(url):
    # Simulate network request
    await asyncio.sleep(2)  # Simulate waiting for 2 seconds
    return f"Data from {url}"

async def process_data(data):
    await asyncio.sleep(1) #Simulate processing
    return f"Processed: {data}"

async def main():
    print("Start")
    data = await fetch_data("https://example.com/api/data")  # Pause here
    result = await process_data(data)
    print(result)  # This line executes *after* fetch_data completes
    print("End")

# Run the main function
asyncio.run(main())