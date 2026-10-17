# Input cache hit rate

Hit rate = cached input tokens / all input tokens of the move requests, read from every provider response (claude cache_read_input_tokens, codex cached_input_tokens, OpenAI-compatible prompt_tokens_details.cached_tokens). Warm = without each game's first 3 moves of the player.

## Current tournament (aichess-0045-20261017-034241)

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 135 | 8009791 | 6430208 | 80.3% | 80.4% |
| GLM 5.3 Flash | 90 | 3382172 | 3025728 | 89.5% | 89.9% |
| GPT-6.1 Sol | 154 | 6369205 | 6038528 | 94.8% | 95.3% |
| Haiku 5.5 | 109 | 4761400 | 4509093 | 94.7% | 95.2% |
| Sonnet 5.5 | 119 | 5371076 | 4901083 | 91.2% | 91.8% |

## All tournaments

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 10659 | 142891173 | 90798464 | 63.5% | 63.6% |
| Fable 5.1 | 179 | 3913645 | 3703873 | 94.6% | 95.5% |
| GLM 5.3 Flash | 1735 | 38453224 | 32920320 | 85.6% | 86.2% |
| GPT-6 Astra | 456 | 15632539 | 14922624 | 95.5% | 95.9% |
| GPT-6.1 Sol | 9901 | 305430674 | 284721920 | 93.2% | 93.8% |
| Haiku 5.5 | 433 | 21187192 | 20259365 | 95.6% | 96.0% |
| Sonnet 5.5 | 10285 | 262379044 | 250532394 | 95.5% | 96.2% |
