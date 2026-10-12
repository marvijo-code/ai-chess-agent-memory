# Input cache hit rate

Hit rate = cached input tokens / all input tokens of the move requests, read from every provider response (claude cache_read_input_tokens, codex cached_input_tokens, OpenAI-compatible prompt_tokens_details.cached_tokens). Warm = without each game's first 3 moves of the player.

## Current tournament (aichess-0037-20261012-162646)

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 178 | 3931677 | 3687168 | 93.8% | 94.3% |
| Fable 5.1 | 78 | 1115280 | 1017793 | 91.3% | 92.4% |
| GLM 5.3 Flash | 163 | 3575651 | 3352832 | 93.8% | 94.2% |
| GPT-6 Astra | 217 | 6832606 | 6528768 | 95.6% | 95.9% |
| GPT-6.1 Sol | 208 | 6940483 | 6458112 | 93.0% | 93.6% |
| Sonnet 5.5 | 202 | 5541519 | 5309455 | 95.8% | 96.7% |

## All tournaments

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 9274 | 108915744 | 61337984 | 56.3% | 56.3% |
| Fable 5.1 | 78 | 1115280 | 1017793 | 91.3% | 92.4% |
| GLM 5.3 Flash | 616 | 10081330 | 9072576 | 90.0% | 90.6% |
| GPT-6 Astra | 217 | 6832606 | 6528768 | 95.6% | 95.9% |
| GPT-6.1 Sol | 8044 | 240994109 | 224504704 | 93.2% | 93.7% |
| Sonnet 5.5 | 8039 | 182975359 | 174787515 | 95.5% | 96.2% |
