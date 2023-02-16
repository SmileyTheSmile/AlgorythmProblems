import problems as prob


def main():
    print(f"""
    Valid parentheses: {prob.valid_parentheses('(([{}]))[')}
    Letter counter: {prob.count_letters_in_word_variations('hello')}
    
    """)


if __name__ == "__main__":
    main()