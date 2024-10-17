
# GTFS-RT Trip Updates Reader

This project retrieves and decodes GTFS-RT trip updates from an API using Python. The response is in Protocol Buffers format and is converted to human-readable JSON.

## Prerequisites

Before running this project, make sure you have Python 3.6+ installed on your machine.

## Setup

### 1. Clone the repository

To clone the repository, use the following command:

```bash
git clone https://github.com/your-username/your-repo-name.git
```

Replace `your-username` and `your-repo-name` with the appropriate GitHub username and repository name.

### 2. Navigate to the project directory

```bash
cd your-repo-name
```

### 3. Create a virtual environment

It is recommended to create a virtual environment to manage dependencies:

```bash
python3 -m venv venv
```

### 4. Activate the virtual environment

#### On macOS or Linux:
```bash
source venv/bin/activate
```

#### On Windows:
```bash
.env\Scriptsctivate
```

### 5. Install the required dependencies

With the virtual environment activated, install the required dependencies from the `requirements.txt` file:

```bash
pip install -r requirements.txt
```

### 6. Add your API key

Create a `.env` file in the root directory of the project and add your API key to it:

```bash
API_KEY=your_api_key_here
```

Make sure to replace `your_api_key_here` with the actual API key.

## Running the Project

To run the project, execute the `main.py` file:

```bash
python main.py
```

This will retrieve the GTFS-RT trip updates, decode the Protocol Buffers format, and output the result as human-readable JSON.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
