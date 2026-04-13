const http = require("http");
const fs = require("fs");
const path = require("path");

const host = "127.0.0.1";
const port = process.env.PORT ? Number(process.env.PORT) : 3000;
const publicDir = path.join(__dirname, "public");

const contentTypes = {
  ".html": "text/html; charset=utf-8",
  ".css": "text/css; charset=utf-8",
  ".js": "application/javascript; charset=utf-8",
  ".json": "application/json; charset=utf-8",
  ".png": "image/png",
  ".jpg": "image/jpeg",
  ".svg": "image/svg+xml",
  ".ico": "image/x-icon",
};

function resolveFile(urlPath) {
  const cleanPath = urlPath === "/" ? "/index.html" : urlPath;
  const decodedPath = decodeURIComponent(cleanPath);
  const relativePath = path.normalize(decodedPath).replace(/^[/\\]+/, "");
  const filePath = path.resolve(publicDir, relativePath);
  const publicRoot = path.resolve(publicDir);

  if (filePath !== publicRoot && !filePath.startsWith(`${publicRoot}${path.sep}`)) {
    return null;
  }

  return filePath;
}

const server = http.createServer((request, response) => {
  const filePath = resolveFile(request.url || "/");

  if (!filePath) {
    response.writeHead(400, { "Content-Type": "text/plain; charset=utf-8" });
    response.end("Bad request");
    return;
  }

  fs.readFile(filePath, (error, data) => {
    if (error) {
      const notFound = error.code === "ENOENT";
      response.writeHead(notFound ? 404 : 500, {
        "Content-Type": "text/plain; charset=utf-8",
      });
      response.end(notFound ? "Not found" : "Server error");
      return;
    }

    const ext = path.extname(filePath).toLowerCase();
    response.writeHead(200, {
      "Content-Type": contentTypes[ext] || "application/octet-stream",
      "Cache-Control": "no-store",
    });
    response.end(data);
  });
});

server.listen(port, host, () => {
  console.log(`Audio Lab running at http://${host}:${port}`);
});
