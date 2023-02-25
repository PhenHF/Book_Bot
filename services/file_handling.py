text = 'book\\2book.txt'
book: dict[int, str] = {}

def _get_part_text(text, start, page_size):
    end = min(start + page_size, len(text))
    for i in range(end, start, -1):
        if text[i-1] in ['..',',','?',':',';','!']:
            break
    else:
        i = end
    page = text[start:i]
    pagelen = len(page)
    return [page, pagelen]


def prepare_book(path: str):
    with open(path, 'r', encoding='UTF-8') as file:
        text = file.read().strip()
    PAGE_SIZE = 920

    pageindex = 0
    for i in range(1, 15):

        book[i] = _get_part_text(text, pageindex, PAGE_SIZE)[0]
        pageindex = pageindex + int(_get_part_text(text, pageindex, PAGE_SIZE)[1])

prepare_book(text)