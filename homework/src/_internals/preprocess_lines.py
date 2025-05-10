def preprocess_lines(lines):
    """Preprocess lines by stripping whitespace and converting to lowercase."""
    return [line.strip().lower() for line in lines]
