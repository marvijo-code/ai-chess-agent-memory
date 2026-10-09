# Input cache hit rate

Hit rate = cached input tokens / all input tokens of the move requests, read from every provider response (claude cache_read_input_tokens, codex cached_input_tokens, OpenAI-compatible prompt_tokens_details.cached_tokens). Warm = without each game's first 3 moves of the player.

## Current tournament (aichess-0006-20261009-001831)

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 231 | 2970644 | 1404032 | 47.3% | 47.2% |
| GPT-6.1 Sol | 111 | 2697508 | 2431104 | 90.1% | 90.8% |
| Sonnet 5.5 | 135 | 2961671 | 2821778 | 95.3% | 95.9% |

## All tournaments

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 1625 | 18340235 | 8464768 | 46.2% | 46.1% |
| GPT-6.1 Sol | 1281 | 37536162 | 35026816 | 93.3% | 93.7% |
| Sonnet 5.5 | 1361 | 30950911 | 29616876 | 95.7% | 96.2% |
