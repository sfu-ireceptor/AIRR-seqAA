FROM debian:stable-slim
RUN apt-get update && apt-get install -y --no-install-recommends \
  bash \
  ca-certificates \
  curl \
  python3 \
  python3-pandas \
  && rm -rf /var/lib/apt/lists/*
COPY adaptive/iseq/iseq /usr/local/bin/
COPY scripts/tsv_to_json.py /usr/local/bin/
