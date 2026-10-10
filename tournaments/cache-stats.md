# Input cache hit rate

Hit rate = cached input tokens / all input tokens of the move requests, read from every provider response (claude cache_read_input_tokens, codex cached_input_tokens, OpenAI-compatible prompt_tokens_details.cached_tokens). Warm = without each game's first 3 moves of the player.

## Current tournament (aichess-0021-20261010-172846)

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 113 | 1208156 | 686592 | 56.8% | 56.8% |
| GPT-6.1 Sol | 71 | 1694311 | 1585792 | 93.6% | 94.0% |
| Sonnet 5.5 | 52 | 784125 | 723892 | 92.3% | 93.8% |

## All tournaments

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 5487 | 60865468 | 29474304 | 48.4% | 48.4% |
| GPT-6.1 Sol | 4502 | 131112905 | 121915264 | 93.0% | 93.4% |
| Sonnet 5.5 | 4733 | 105324371 | 100647405 | 95.6% | 96.2% |
