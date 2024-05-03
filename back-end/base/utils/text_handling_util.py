from base.utils.gemini_util import generate_text

def text_handling_util(text) -> str:
    """
        Обработка текста

        :param text: Текст
        :return: Обработанный текст
    """
    text = text.split('---------------------------------------------------------')
    all_products = text[2].split('\n')
    products, p = " ", " "

    for product in all_products:
        p += product
        p += ' '

        if '$' in product:
            products += p
            p = "; "

    answer = generate_text(products)
    print(answer)

    return answer
