import re


def split_into_sentences(paragraph):
    """
    Splits a paragraph into sentences using regex.
    Handles sentences that may begin with numbers.
    """
    # Split on punctuation followed by space(s)
    sentences = re.split(r'(?<=[.!?])\s+', paragraph.strip())

    # Remove empty strings if any
    sentences = [s for s in sentences if s]

    return sentences


def display_sentences(sentences):
    """
    Displays each sentence and the total count.
    """
    print("\nIndividual Sentences:\n")

    for i, sentence in enumerate(sentences, start=1):
        print(f"{i}. {sentence}")

    print(f"\nTotal number of sentences: {len(sentences)}")


def main():
    """
    Main function to get user input and process it.
    """
    paragraph = input("Enter a paragraph:\n")

    sentences = split_into_sentences(paragraph)
    display_sentences(sentences)


if __name__ == "__main__":
    main()