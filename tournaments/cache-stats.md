# Input cache hit rate

Hit rate = cached input tokens / all input tokens of the move requests, read from every provider response (claude cache_read_input_tokens, codex cached_input_tokens, OpenAI-compatible prompt_tokens_details.cached_tokens). Warm = without each game's first 3 moves of the player.

## Current tournament (aichess-0037-20261012-162646)

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 69 | 1129641 | 1073536 | 95.0% | 96.1% |
| Fable 5.1 | 78 | 1115280 | 1017793 | 91.3% | 92.4% |
| GLM 5.3 Flash | 77 | 1225730 | 1158912 | 94.5% | 95.3% |
| GPT-6 Astra | 148 | 5261064 | 5063296 | 96.2% | 96.4% |
| GPT-6.1 Sol | 147 | 5292939 | 4979072 | 94.1% | 94.6% |
| Sonnet 5.5 | 134 | 3938151 | 3773926 | 95.8% | 96.7% |

## All tournaments

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 9165 | 106113708 | 58724352 | 55.3% | 55.3% |
| Fable 5.1 | 78 | 1115280 | 1017793 | 91.3% | 92.4% |
| GLM 5.3 Flash | 530 | 7731409 | 6878656 | 89.0% | 89.7% |
| GPT-6 Astra | 148 | 5261064 | 5063296 | 96.2% | 96.4% |
| GPT-6.1 Sol | 7983 | 239346565 | 223025664 | 93.2% | 93.7% |
| Sonnet 5.5 | 7971 | 181371991 | 173251986 | 95.5% | 96.2% |
