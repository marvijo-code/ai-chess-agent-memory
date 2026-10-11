# Input cache hit rate

Hit rate = cached input tokens / all input tokens of the move requests, read from every provider response (claude cache_read_input_tokens, codex cached_input_tokens, OpenAI-compatible prompt_tokens_details.cached_tokens). Warm = without each game's first 3 moves of the player.

## Current tournament (aichess-0030-20261011-145519)

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 198 | 2024012 | 1111552 | 54.9% | 54.9% |
| GPT-6.1 Sol | 187 | 5842953 | 5418624 | 92.7% | 93.2% |
| Sonnet 5.5 | 133 | 2788511 | 2647795 | 95.0% | 96.0% |

## All tournaments

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 8022 | 89410379 | 45901824 | 51.3% | 51.3% |
| GPT-6.1 Sol | 6413 | 186467552 | 173620992 | 93.1% | 93.6% |
| Sonnet 5.5 | 6508 | 142150591 | 135643245 | 95.4% | 96.1% |
