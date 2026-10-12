# Input cache hit rate

Hit rate = cached input tokens / all input tokens of the move requests, read from every provider response (claude cache_read_input_tokens, codex cached_input_tokens, OpenAI-compatible prompt_tokens_details.cached_tokens). Warm = without each game's first 3 moves of the player.

## Current tournament (aichess-0037-20261012-162646)

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 178 | 3931677 | 3687168 | 93.8% | 94.3% |
| Fable 5.1 | 98 | 1355940 | 1229612 | 90.7% | 92.5% |
| GLM 5.3 Flash | 185 | 3805248 | 3543552 | 93.1% | 93.7% |
| GPT-6 Astra | 257 | 7989138 | 7613440 | 95.3% | 95.9% |
| GPT-6.1 Sol | 208 | 6940483 | 6458112 | 93.0% | 93.6% |
| Sonnet 5.5 | 223 | 6308135 | 6059901 | 96.1% | 96.8% |

## All tournaments

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 9274 | 108915744 | 61337984 | 56.3% | 56.3% |
| Fable 5.1 | 98 | 1355940 | 1229612 | 90.7% | 92.5% |
| GLM 5.3 Flash | 638 | 10310927 | 9263296 | 89.8% | 90.5% |
| GPT-6 Astra | 257 | 7989138 | 7613440 | 95.3% | 95.9% |
| GPT-6.1 Sol | 8044 | 240994109 | 224504704 | 93.2% | 93.7% |
| Sonnet 5.5 | 8060 | 183741975 | 175537961 | 95.5% | 96.2% |
