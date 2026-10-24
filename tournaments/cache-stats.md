# Input cache hit rate

Hit rate = cached input tokens / all input tokens of the move requests, read from every provider response (claude cache_read_input_tokens, codex cached_input_tokens, OpenAI-compatible prompt_tokens_details.cached_tokens). Warm = without each game's first 3 moves of the player.

## Current tournament (aichess-0060-20261022-215721)

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 261 | 18223774 | 16881536 | 92.6% | 92.8% |
| DeepSeek V4.1 Flash 1017 | 150 | 6332592 | 5626496 | 88.8% | 89.2% |
| GLM 5.3 Flash | 193 | 11569209 | 8685632 | 75.1% | 75.5% |

## All tournaments

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 13148 | 273068019 | 205861120 | 75.4% | 75.6% |
| DeepSeek V4.1 Flash 1017 | 2350 | 110032928 | 97442424 | 88.6% | 88.8% |
| Fable 5.1 | 179 | 3913645 | 3703873 | 94.6% | 95.5% |
| GLM 5.3 Flash | 3861 | 116164569 | 92065264 | 79.3% | 79.8% |
| GPT-6 Astra | 456 | 15632539 | 14922624 | 95.5% | 95.9% |
| GPT-6.1 Sol | 10063 | 311254406 | 290190080 | 93.2% | 93.8% |
| Haiku 5.5 | 603 | 31298164 | 29862221 | 95.4% | 95.8% |
| Sonnet 5.5 | 10538 | 274527705 | 261922704 | 95.4% | 96.1% |
