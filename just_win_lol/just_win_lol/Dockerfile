# FROM golang:1.22 AS build
# WORKDIR /justwinapp
# COPY go.mod go.sum /justwinapp/
# RUN go mod download
# COPY *.go /justwinapp/
# RUN CGO_ENABLED=0 GOOS=linux go build -o /just-win-lol



# FROM alpine:latest AS run
# WORKDIR /justwinapp
# RUN adduser -S jelly
# USER jelly
# COPY --chown=jelly assets /justwinapp/assets
# COPY --from=build --chown=jelly /just-win-lol /justwinapp/
# EXPOSE 8080
# ENTRYPOINT ["/justwinapp/just-win-lol"]

# taken from https://templ.guide/quick-start/installation#docker
# Fetch
FROM golang:latest AS fetch-stage
COPY go.mod go.sum /app/
WORKDIR /app
RUN go mod download

# Generate
FROM ghcr.io/a-h/templ:latest AS generate-stage
COPY --chown=65532:65532 . /app
WORKDIR /app
RUN ["templ", "generate"]

# Build
FROM golang:latest AS build-stage
COPY --from=generate-stage /app /app
WORKDIR /app
RUN CGO_ENABLED=0 GOOS=linux go build -o /just-win-lol

# Deploy
# FROM gcr.io/distroless/base-debian12 AS deploy-stage
# WORKDIR /
# COPY --from=build-stage /app/app /app
# EXPOSE 8080
# USER nonroot:nonroot
# ENTRYPOINT ["/app"]

FROM alpine:latest AS run
WORKDIR /app
RUN adduser -S jelly
USER jelly
COPY --chown=jelly assets /app/assets
COPY --from=build-stage --chown=jelly /just-win-lol /app/
EXPOSE 8080
ENTRYPOINT ["/app/just-win-lol"]