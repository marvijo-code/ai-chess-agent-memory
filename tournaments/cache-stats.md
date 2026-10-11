# Input cache hit rate

Hit rate = cached input tokens / all input tokens of the move requests, read from every provider response (claude cache_read_input_tokens, codex cached_input_tokens, OpenAI-compatible prompt_tokens_details.cached_tokens). Warm = without each game's first 3 moves of the player.

## Current tournament (aichess-0024-20261011-001419)

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 217 | 2321924 | 1300992 | 56.0% | 56.0% |
| GPT-6.1 Sol | 187 | 6199277 | 5837312 | 94.2% | 94.4% |
| Sonnet 5.5 | 160 | 3458853 | 3293301 | 95.2% | 95.9% |

## All tournaments

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 6405 | 71158055 | 35575296 | 50.0% | 49.9% |
| GPT-6.1 Sol | 5169 | 149715099 | 139334656 | 93.1% | 93.5% |
| Sonnet 5.5 | 5404 | 119512066 | 114134209 | 95.5% | 96.1% |
