# Input cache hit rate

Hit rate = cached input tokens / all input tokens of the move requests, read from every provider response (claude cache_read_input_tokens, codex cached_input_tokens, OpenAI-compatible prompt_tokens_details.cached_tokens). Warm = without each game's first 3 moves of the player.

## Current tournament (aichess-0037-20261012-162646)

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 236 | 4652753 | 4338560 | 93.2% | 93.9% |
| Fable 5.1 | 179 | 3913645 | 3703873 | 94.6% | 95.5% |
| GLM 5.3 Flash | 219 | 4282228 | 3921152 | 91.6% | 92.1% |
| GPT-6 Astra | 368 | 11669770 | 11094784 | 95.1% | 95.6% |
| GPT-6.1 Sol | 306 | 10623433 | 9932160 | 93.5% | 94.0% |
| Sonnet 5.5 | 432 | 14366026 | 13926017 | 96.9% | 97.5% |

## All tournaments

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 9332 | 109636820 | 61989376 | 56.5% | 56.5% |
| Fable 5.1 | 179 | 3913645 | 3703873 | 94.6% | 95.5% |
| GLM 5.3 Flash | 672 | 10787907 | 9640896 | 89.4% | 90.0% |
| GPT-6 Astra | 368 | 11669770 | 11094784 | 95.1% | 95.6% |
| GPT-6.1 Sol | 8142 | 244677059 | 227978752 | 93.2% | 93.7% |
| Sonnet 5.5 | 8269 | 191799866 | 183404077 | 95.6% | 96.3% |
