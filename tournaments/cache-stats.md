# Input cache hit rate

Hit rate = cached input tokens / all input tokens of the move requests, read from every provider response (claude cache_read_input_tokens, codex cached_input_tokens, OpenAI-compatible prompt_tokens_details.cached_tokens). Warm = without each game's first 3 moves of the player.

## Current tournament (aichess-0022-20261010-192853)

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 181 | 1764067 | 952832 | 54.0% | 53.8% |
| GPT-6.1 Sol | 103 | 1962428 | 1799296 | 91.7% | 92.3% |
| Sonnet 5.5 | 134 | 2691364 | 2548112 | 94.7% | 95.6% |

## All tournaments

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 5840 | 64828158 | 31863808 | 49.2% | 49.1% |
| GPT-6.1 Sol | 4729 | 136456813 | 126932608 | 93.0% | 93.5% |
| Sonnet 5.5 | 4984 | 110411189 | 105467389 | 95.5% | 96.1% |
