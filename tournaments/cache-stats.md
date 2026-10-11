# Input cache hit rate

Hit rate = cached input tokens / all input tokens of the move requests, read from every provider response (claude cache_read_input_tokens, codex cached_input_tokens, OpenAI-compatible prompt_tokens_details.cached_tokens). Warm = without each game's first 3 moves of the player.

## Current tournament (aichess-0028-20261011-102906)

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 264 | 3285431 | 2042368 | 62.2% | 62.2% |
| GPT-6.1 Sol | 209 | 7340011 | 6958336 | 94.8% | 95.1% |
| Sonnet 5.5 | 165 | 3480805 | 3319023 | 95.4% | 96.1% |

## All tournaments

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 7526 | 84331891 | 43087872 | 51.1% | 51.0% |
| GPT-6.1 Sol | 6040 | 176566737 | 164572544 | 93.2% | 93.6% |
| Sonnet 5.5 | 6199 | 136497553 | 130323743 | 95.5% | 96.1% |
