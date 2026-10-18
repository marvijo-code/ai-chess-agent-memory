# Input cache hit rate

Hit rate = cached input tokens / all input tokens of the move requests, read from every provider response (claude cache_read_input_tokens, codex cached_input_tokens, OpenAI-compatible prompt_tokens_details.cached_tokens). Warm = without each game's first 3 moves of the player.

## Current tournament (aichess-0047-20261017-154745)

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 34 | 1608733 | 1310080 | 81.4% | 81.7% |
| DeepSeek V4.1 Flash 1017 | 20 | 509660 | 433920 | 85.1% | 85.5% |
| GLM 5.3 Flash | 20 | 706543 | 380288 | 53.8% | 54.6% |
| Haiku 5.5 | 33 | 1525958 | 1423829 | 93.3% | 93.9% |
| Sonnet 5.5 | 52 | 2024430 | 1853834 | 91.6% | 92.1% |

## All tournaments

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 10855 | 152611212 | 99070720 | 64.9% | 65.0% |
| DeepSeek V4.1 Flash 1017 | 20 | 509660 | 433920 | 85.1% | 85.5% |
| Fable 5.1 | 179 | 3913645 | 3703873 | 94.6% | 95.5% |
| GLM 5.3 Flash | 1860 | 43807820 | 36648704 | 83.7% | 84.2% |
| GPT-6 Astra | 456 | 15632539 | 14922624 | 95.5% | 95.9% |
| GPT-6.1 Sol | 10063 | 311254406 | 290190080 | 93.2% | 93.8% |
| Haiku 5.5 | 603 | 31298164 | 29862221 | 95.4% | 95.8% |
| Sonnet 5.5 | 10538 | 274527705 | 261922704 | 95.4% | 96.1% |
