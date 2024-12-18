#!/bin/env python

class Citation:
    def __init__(self, title, authors, conference, location, year, url) -> None:
        self.title = title
        self.authors = authors
        self.url = url
        self.conference = conference
        self.location = location
        self.year = year

    @classmethod
    def from_bibtex(cls, bibtext: str):
        authors = ""
        title = ""
        url = ""
        conference = ""
        location = ""
        year = ""
        url = ""
        strip_chars = ' ",'
        for line in bibtext.splitlines():
            line = line.strip()
            if line.startswith("author"):
                _, authors = line.split(sep="=", maxsplit=2)
                authors = authors.replace("Martin Kocour", "<b>Martin Kocour</b>")
                authors = authors.strip(strip_chars).split(" and ")
            if line.startswith("title"):
                _, title = line.split(sep="=", maxsplit=2)
                title = title.strip(strip_chars)
            if line.startswith("booktitle"):
                _, conference = line.split(sep="=", maxsplit=2)
                conference = conference.strip(strip_chars)
            if line.startswith("location"):
                _, location = line.split(sep="=", maxsplit=2)
                location = location.strip(strip_chars)
            if line.startswith("year"):
                _, year = line.split(sep="=", maxsplit=2)
                year = year.strip(strip_chars)
            if line.startswith("url"):
                _, url = line.split(sep="=", maxsplit=2)
                url = url.strip(strip_chars)

        return cls(title, authors, conference, location, year, url)

    def to_post(self):
        post = (
            "---\n"
            "layout: post\n"
            f'title: "{self.title}"\n'
            f'date:  {self.year}-03-25 22:20:59 +00:00\n'
            f'image: /images/placeholder.jpg\n'
            "categories: research\n"
            f'authors: "{", ".join(self.authors)}"\n'
            f'venue: "{self.conference}, {self.location}"\n'
            f'url: {self.url}\n'
            "---\n"
        )
        return post


def main():
    import sys
    if len(sys.argv) < 2:
        print(f"{sys.argv[0]} file.bibtext|-")
        sys.exit(1)

    if sys.argv[1] == "-":
        citation = Citation.from_bibtex(sys.stdin.read())
    else:
        with open(sys.argv[1]) as f:
            citation = Citation.from_bibtex(f.read())

    print(citation.to_post())

if __name__ == "__main__":
    main()
