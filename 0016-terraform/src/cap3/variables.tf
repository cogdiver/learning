variable "nouns" {
    description = "A list of nouns"
    type = list(string)
}

variable "adjectives" {
    description = "A list of adjectives"
    type = list(string)
}

variable "verbs" {
    description = "A list of verbs"
    type = list(string)
}

variable "adverbs" {
    description = "A list of adverbs"
    type = list(string)
}

variable "numbers" {
    description = "A list of numbers"
    type = list(number)
}

variable "words" {
    description = "A word pool to use for Mad Libs"
    type = object({
        nouns = list(string),
        adjectives = list(string),
        verbs = list(string),
        adverbs = list(string),
        numbers = list(number),
    })
}
