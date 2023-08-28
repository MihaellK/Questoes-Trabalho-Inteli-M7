/** @type {import('next').NextConfig} */
const nextConfig = {
    async rewrites() {
        return [
          {
            source: "/api/todos",
            destination: "http://127.0.0.1:8000/notes/",
          },
        //   {
        //     source: "/api/new-todo",
        //     destination: "http://127.0.0.1:8000/users/1/notes/"
        //   },
        ];
      },
}

module.exports = nextConfig
