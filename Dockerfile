FROM debian:testing-slim
RUN apt-get update && apt-get install -y --no-install-recommends \
  bash \
  ca-certificates \
  curl \
  python3 \
  python3-ipython \
  python3-pandas \
  && rm -rf /var/lib/apt/lists/*
COPY adaptive/iseq/iseq /usr/local/bin/
COPY scripts/*.py /usr/local/bin/
