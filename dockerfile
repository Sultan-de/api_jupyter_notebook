FROM python:3.10


# Configure Poetry
ENV POETRY_VERSION=1.1.13
ENV POETRY_HOME=/opt/poetry
ENV POETRY_VENV=/opt/poetry-venv
ENV POETRY_CACHE_DIR=/opt/.cache

# This is wrong!
# Install poetry separated from system interpreter
RUN python3 -m venv $POETRY_VENV \
    && $POETRY_VENV/bin/pip install -U pip setuptools \
    && $POETRY_VENV/bin/pip install poetry==${POETRY_VERSION}

# Add `poetry` to PATH
ENV PATH="${PATH}:${POETRY_VENV}/bin"

WORKDIR /api_jupyter_notebook

# Install dependencies
COPY poetry.lock pyproject.toml ./
#RUN poetry add requests
RUN poetry install

# Run your app
COPY . /api_jupyter_notebook
CMD [ "poetry", "run", "python", "main.py", "print('Hello, World!')" ]


#RUN apk --update --no-cache add curl
RUN pip install --no-cache-dir --upgrade pip && \
	pip install --no-cache-dir python-dotenv

