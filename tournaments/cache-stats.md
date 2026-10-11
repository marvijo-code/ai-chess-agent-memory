# Input cache hit rate

Hit rate = cached input tokens / all input tokens of the move requests, read from every provider response (claude cache_read_input_tokens, codex cached_input_tokens, OpenAI-compatible prompt_tokens_details.cached_tokens). Warm = without each game's first 3 moves of the player.

## Current tournament (aichess-0027-20261011-075651)

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 108 | 952932 | 457216 | 48.0% | 47.7% |
| GPT-6.1 Sol | 122 | 3828297 | 3527296 | 92.1% | 92.5% |
| Sonnet 5.5 | 124 | 2769462 | 2649386 | 95.7% | 96.4% |

## All tournaments

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 7152 | 79738394 | 40267264 | 50.5% | 50.4% |
| GPT-6.1 Sol | 5666 | 163982032 | 152650496 | 93.1% | 93.5% |
| Sonnet 5.5 | 5951 | 131202026 | 125274584 | 95.5% | 96.1% |
