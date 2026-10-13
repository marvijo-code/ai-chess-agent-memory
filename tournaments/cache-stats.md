# Input cache hit rate

Hit rate = cached input tokens / all input tokens of the move requests, read from every provider response (claude cache_read_input_tokens, codex cached_input_tokens, OpenAI-compatible prompt_tokens_details.cached_tokens). Warm = without each game's first 3 moves of the player.

## Current tournament (aichess-0041-20261013-124210)

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 48 | 852236 | 808832 | 94.9% | 95.6% |
| GPT-6.1 Sol | 45 | 1409582 | 1244672 | 88.3% | 88.6% |
| Sonnet 5.5 | 47 | 1348428 | 1250890 | 92.8% | 93.6% |

## All tournaments

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 10032 | 121959071 | 73281792 | 60.1% | 60.1% |
| Fable 5.1 | 179 | 3913645 | 3703873 | 94.6% | 95.5% |
| GLM 5.3 Flash | 1118 | 18161189 | 15901376 | 87.6% | 88.3% |
| GPT-6 Astra | 456 | 15632539 | 14922624 | 95.5% | 95.9% |
| GPT-6.1 Sol | 8978 | 271632193 | 252891520 | 93.1% | 93.6% |
| Sonnet 5.5 | 9314 | 223192284 | 213631948 | 95.7% | 96.4% |
