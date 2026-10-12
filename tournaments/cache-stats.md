# Input cache hit rate

Hit rate = cached input tokens / all input tokens of the move requests, read from every provider response (claude cache_read_input_tokens, codex cached_input_tokens, OpenAI-compatible prompt_tokens_details.cached_tokens). Warm = without each game's first 3 moves of the player.

## Current tournament (aichess-0036-20261012-121058)

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 192 | 3441039 | 3183488 | 92.5% | 93.4% |
| GLM 5.3 Flash | 165 | 2721186 | 2480896 | 91.2% | 91.8% |
| GPT-6.1 Sol | 236 | 7942992 | 7377152 | 92.9% | 93.6% |
| Sonnet 5.5 | 229 | 6333967 | 6093356 | 96.2% | 97.1% |

## All tournaments

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 9069 | 104626358 | 57327488 | 54.8% | 54.8% |
| GLM 5.3 Flash | 453 | 6505679 | 5719744 | 87.9% | 88.6% |
| GPT-6.1 Sol | 7660 | 225453748 | 209760256 | 93.0% | 93.5% |
| Sonnet 5.5 | 7810 | 176870438 | 168950318 | 95.5% | 96.2% |
