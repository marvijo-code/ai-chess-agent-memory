# Input cache hit rate

Hit rate = cached input tokens / all input tokens of the move requests, read from every provider response (claude cache_read_input_tokens, codex cached_input_tokens, OpenAI-compatible prompt_tokens_details.cached_tokens). Warm = without each game's first 3 moves of the player.

## Current tournament (aichess-0037-20261012-162646)

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 159 | 3759070 | 3547776 | 94.4% | 94.8% |
| Fable 5.1 | 78 | 1115280 | 1017793 | 91.3% | 92.4% |
| GLM 5.3 Flash | 163 | 3575651 | 3352832 | 93.8% | 94.2% |
| GPT-6 Astra | 191 | 6329338 | 6051840 | 95.6% | 95.9% |
| GPT-6.1 Sol | 189 | 6546456 | 6118016 | 93.5% | 93.9% |
| Sonnet 5.5 | 175 | 4990624 | 4792818 | 96.0% | 96.8% |

## All tournaments

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 9255 | 108743137 | 61198592 | 56.3% | 56.3% |
| Fable 5.1 | 78 | 1115280 | 1017793 | 91.3% | 92.4% |
| GLM 5.3 Flash | 616 | 10081330 | 9072576 | 90.0% | 90.6% |
| GPT-6 Astra | 191 | 6329338 | 6051840 | 95.6% | 95.9% |
| GPT-6.1 Sol | 8025 | 240600082 | 224164608 | 93.2% | 93.7% |
| Sonnet 5.5 | 8012 | 182424464 | 174270878 | 95.5% | 96.2% |
