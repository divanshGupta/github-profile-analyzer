BASE URL
http://127.0.0.1:5000

1. GET /user/<username>
eg.: 
/user/divanshGupta
response: 
{
  "account_age": 7,
  "followers": 2,
  "public_repos": 31,
  "username": "divanshGupta"
}

2. GET /user/<username>/repos
eg.:
/user/divanshGupta/repos?limit=5
response:
{
  "top_repositories": [
    {
      "language": "TypeScript",
      "name": "ai-wrapper",
      "repo_url": "https://github.com/divanshGupta/ai-wrapper",
      "stars": 0
    },
    {
      "language": "JavaScript",
      "name": "backend",
      "repo_url": "https://github.com/divanshGupta/backend",
      "stars": 0
    },
    {
      "language": "CSS",
      "name": "bubble-2",
      "repo_url": "https://github.com/divanshGupta/bubble-2",
      "stars": 0
    },
    {
      "language": "HTML",
      "name": "cuberto",
      "repo_url": "https://github.com/divanshGupta/cuberto",
      "stars": 0
    },
    {
      "language": null,
      "name": "divanshGupta",
      "repo_url": "https://github.com/divanshGupta/divanshGupta",
      "stars": 0
    }
  ],
  "username": "divanshGupta"
}