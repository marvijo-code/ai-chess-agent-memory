# Input cache hit rate

Hit rate = cached input tokens / all input tokens of the move requests, read from every provider response (claude cache_read_input_tokens, codex cached_input_tokens, OpenAI-compatible prompt_tokens_details.cached_tokens). Warm = without each game's first 3 moves of the player.

## Current tournament (aichess-0037-20261012-162646)

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 236 | 4652753 | 4338560 | 93.2% | 93.9% |
| Fable 5.1 | 150 | 2556878 | 2372619 | 92.8% | 94.1% |
| GLM 5.3 Flash | 185 | 3805248 | 3543552 | 93.1% | 93.7% |
| GPT-6 Astra | 304 | 9222185 | 8764672 | 95.0% | 95.6% |
| GPT-6.1 Sol | 208 | 6940483 | 6458112 | 93.0% | 93.6% |
| Sonnet 5.5 | 251 | 6893738 | 6610208 | 95.9% | 96.8% |

## All tournaments

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 9332 | 109636820 | 61989376 | 56.5% | 56.5% |
| Fable 5.1 | 150 | 2556878 | 2372619 | 92.8% | 94.1% |
| GLM 5.3 Flash | 638 | 10310927 | 9263296 | 89.8% | 90.5% |
| GPT-6 Astra | 304 | 9222185 | 8764672 | 95.0% | 95.6% |
| GPT-6.1 Sol | 8044 | 240994109 | 224504704 | 93.2% | 93.7% |
| Sonnet 5.5 | 8088 | 184327578 | 176088268 | 95.5% | 96.2% |
