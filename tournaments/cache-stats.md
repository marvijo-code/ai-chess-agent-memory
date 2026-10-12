# Input cache hit rate

Hit rate = cached input tokens / all input tokens of the move requests, read from every provider response (claude cache_read_input_tokens, codex cached_input_tokens, OpenAI-compatible prompt_tokens_details.cached_tokens). Warm = without each game's first 3 moves of the player.

## Current tournament (aichess-0037-20261012-162646)

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 69 | 1129641 | 1073536 | 95.0% | 96.1% |
| Fable 5.1 | 78 | 1115280 | 1017793 | 91.3% | 92.4% |
| GLM 5.3 Flash | 77 | 1225730 | 1158912 | 94.5% | 95.3% |
| GPT-6 Astra | 185 | 6086508 | 5815296 | 95.5% | 95.8% |
| GPT-6.1 Sol | 184 | 6305740 | 5881088 | 93.3% | 93.8% |
| Sonnet 5.5 | 175 | 4990624 | 4792818 | 96.0% | 96.8% |

## All tournaments

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 9165 | 106113708 | 58724352 | 55.3% | 55.3% |
| Fable 5.1 | 78 | 1115280 | 1017793 | 91.3% | 92.4% |
| GLM 5.3 Flash | 530 | 7731409 | 6878656 | 89.0% | 89.7% |
| GPT-6 Astra | 185 | 6086508 | 5815296 | 95.5% | 95.8% |
| GPT-6.1 Sol | 8020 | 240359366 | 223927680 | 93.2% | 93.7% |
| Sonnet 5.5 | 8012 | 182424464 | 174270878 | 95.5% | 96.2% |
