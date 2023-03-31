markdown
# Component Name
ScrapeNikeITPersonas

# Description
This component is designed to scrape information about Nike IT employees from a web page. It's a part of a Yeager Workflow that aims to collect and process employee data for further analysis or reporting.

# Input and Output Models
The component uses Pydantic BaseModel to create input and output data models for type validation and serialization:

- **Input Model**: `ScrapeNikeITPersonasInputDict`: A placeholder input model without any properties.
- **Output Model**: `ScrapeNikeITPersonasOutputDict`: Contains a list of dictionaries containing employee data. Each dictionary has two keys: "name" and "email".

    