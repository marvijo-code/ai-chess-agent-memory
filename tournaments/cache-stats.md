# Input cache hit rate

Hit rate = cached input tokens / all input tokens of the move requests, read from every provider response (claude cache_read_input_tokens, codex cached_input_tokens, OpenAI-compatible prompt_tokens_details.cached_tokens). Warm = without each game's first 3 moves of the player.

## Current tournament (aichess-0022-20261010-192853)

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 35 | 254190 | 120320 | 47.3% | 46.5% |
| GPT-6.1 Sol | 20 | 327874 | 295168 | 90.0% | 90.7% |
| Sonnet 5.5 | 20 | 265956 | 240615 | 90.5% | 92.7% |

## All tournaments

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 5694 | 63318281 | 31031296 | 49.0% | 48.9% |
| GPT-6.1 Sol | 4646 | 134822259 | 125428480 | 93.0% | 93.5% |
| Sonnet 5.5 | 4870 | 107985781 | 103159892 | 95.5% | 96.1% |
