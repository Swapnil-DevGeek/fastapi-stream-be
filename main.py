from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import StreamingResponse
import time

app = FastAPI()

# Allow specific origins
origins = [
    "http://localhost:3000",  # Replace with your frontend's URL
    "http://127.0.0.1:3000",
    "https://stream-fe-ivory.vercel.app"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# A single long paragraph
long_paragraph = """
    This is the first sentence of a very long response. Streaming this data in chunks allows the user to see the text appearing gradually. Each subsequent sentence adds more content, giving the impression of a continuous flow of information. The purpose of this response is to test the streaming capabilities of the backend and frontend integration. 
    Imagine this being a real-time conversation where data is delivered dynamically as it becomes available. With enough content, users can notice the stream unfolding over time. Here is some more filler content to extend the response: lorem ipsum dolor sit amet, consectetur adipiscing elit. 
    Integer nec odio. Praesent libero. Sed cursus ante dapibus diam. Sed nisi. Nulla quis sem at nibh elementum imperdiet. Duis sagittis ipsum. Praesent mauris. Fusce nec tellus sed augue semper porta. Mauris massa. Vestibulum lacinia arcu eget nulla. 
    Class aptent taciti sociosqu ad litora torquent per conubia nostra, per inceptos himenaeos. Curabitur sodales ligula in libero. Sed dignissim lacinia nunc. Curabitur tortor. Pellentesque nibh. Aenean quam. In scelerisque sem at dolor. Maecenas mattis. 
    Sed convallis tristique sem. Proin ut ligula vel nunc egestas porttitor. Morbi lectus risus, iaculis vel, suscipit quis, luctus non, massa. Fusce ac turpis quis ligula lacinia aliquet. Mauris ipsum. Nulla metus metus, ullamcorper vel, tincidunt sed, euismod in, nibh.
"""

def generate_stream():
    sentences = long_paragraph.split(". ")  # Split the paragraph into sentences
    for sentence in sentences:
        yield sentence + ".\n"  # Add a period and newline for formatting
        time.sleep(0.5)  # Simulate streaming by adding delay

@app.get("/stream")
async def stream_response():
    return StreamingResponse(generate_stream(), media_type="text/plain")