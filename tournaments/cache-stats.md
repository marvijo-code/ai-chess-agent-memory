# Input cache hit rate

Hit rate = cached input tokens / all input tokens of the move requests, read from every provider response (claude cache_read_input_tokens, codex cached_input_tokens, OpenAI-compatible prompt_tokens_details.cached_tokens). Warm = without each game's first 3 moves of the player.

## Current tournament (aichess-0038-20261013-003046)

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 89 | 1668165 | 1561984 | 93.6% | 94.1% |
| GLM 5.3 Flash | 60 | 1324887 | 1213440 | 91.6% | 92.0% |
| GPT-6.1 Sol | 33 | 849267 | 777728 | 91.6% | 92.2% |
| Sonnet 5.5 | 60 | 1317503 | 1241946 | 94.3% | 96.0% |

## All tournaments

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 9421 | 111304985 | 63551360 | 57.1% | 57.1% |
| Fable 5.1 | 179 | 3913645 | 3703873 | 94.6% | 95.5% |
| GLM 5.3 Flash | 732 | 12112794 | 10854336 | 89.6% | 90.2% |
| GPT-6 Astra | 456 | 15632539 | 14922624 | 95.5% | 95.9% |
| GPT-6.1 Sol | 8218 | 246805827 | 229961600 | 93.2% | 93.7% |
| Sonnet 5.5 | 8373 | 194255188 | 185734239 | 95.6% | 96.3% |
