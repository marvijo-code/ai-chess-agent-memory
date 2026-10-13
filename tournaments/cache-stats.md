# Input cache hit rate

Hit rate = cached input tokens / all input tokens of the move requests, read from every provider response (claude cache_read_input_tokens, codex cached_input_tokens, OpenAI-compatible prompt_tokens_details.cached_tokens). Warm = without each game's first 3 moves of the player.

## Current tournament (aichess-0038-20261013-003046)

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 29 | 372798 | 326144 | 87.5% | 88.4% |
| GPT-6.1 Sol | 33 | 849267 | 777728 | 91.6% | 92.2% |
| Sonnet 5.5 | 28 | 589630 | 553044 | 93.8% | 95.7% |

## All tournaments

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 9361 | 110009618 | 62315520 | 56.6% | 56.6% |
| Fable 5.1 | 179 | 3913645 | 3703873 | 94.6% | 95.5% |
| GLM 5.3 Flash | 672 | 10787907 | 9640896 | 89.4% | 90.0% |
| GPT-6 Astra | 456 | 15632539 | 14922624 | 95.5% | 95.9% |
| GPT-6.1 Sol | 8218 | 246805827 | 229961600 | 93.2% | 93.7% |
| Sonnet 5.5 | 8341 | 193527315 | 185045337 | 95.6% | 96.3% |
