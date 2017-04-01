import glob
import re
import sys
from typing import List, NamedTuple, Pattern

misused_file_name = 'scripts/frequently_misused.txt'
posts_folder = '_posts'
drafts_folder = '_drafts'


def get_post_paths(include_drafts=True) -> List[str]:
    posts = glob.glob(posts_folder + '/**/*.md', recursive=True)
    drafts = glob.glob(drafts_folder + '/**/*.md', recursive=True)

    if include_drafts:
        return posts + drafts

    return posts


class FileContents(NamedTuple):
    file_path: str
    lines: List[str]
    front_matter_length: int


def get_file_content(file_path: str) -> FileContents:
    with open(file_path, encoding='utf-8') as file:
        lines = file.read().splitlines()

    dash_indices = []

    for i, line in enumerate(lines):
        if line.startswith('---'):
            dash_indices.append(i)

    assert len(dash_indices) >= 2

    return FileContents(file_path, lines[dash_indices[1] + 1:], dash_indices[1] + 2)


def read_in_misused_words(src_file_name: str) -> List[Pattern]:
    with open(src_file_name) as file:
        lines = file.read().splitlines()

    words = (word for word in lines if word and not word.startswith('#'))

    regex_template = r'\b({})\b'
    patterns = [re.compile(regex_template.format(word)) for word in words]

    return patterns


def check_file_word_usage(file: FileContents, patterns: List[Pattern]):
    for line_num, line in enumerate(file.lines):
        for pattern in patterns:
            match = pattern.search(line)
            if match:
                adjusted_line_number = line_num + file.front_matter_length
                error = match.group(1)

                print('Found \'{}\' on line {} of {}'.format(error, adjusted_line_number, file.file_path))


def misused_words():
    patterns = read_in_misused_words(misused_file_name)
    file_contents = (get_file_content(file_name) for file_name in get_post_paths())

    for file_content in file_contents:
        check_file_word_usage(file_content, patterns)


def main(args):
    misused_words()

if __name__ == '__main__':
    main(sys.argv)
