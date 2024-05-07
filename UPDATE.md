# Major Update History and Explanation
If you have any concern about the update, you can argue in the issue! More discussion is welcome!

重大なアップデートに関して、疑念がある場合は、Issueで議論を投稿できます。日本語でも大丈夫です。

## v0.2.0
In this update, we made the following major changes that affect the evaluation results:
 - Only 0-shot results are employed for the leaderboard.
 - We reject the different prompt selections for each task. Now, the same prompt version is enforced for all tasks.

このアップデートでは、以下の重要な変更を行いました。これらの変更は評価結果に影響を与えます。
 - リーダーボードには0-shotの結果のみを使用します。
 - 各タスクごとに異なるプロンプトを利用することを禁じます。今後は、すべてのタスクに同じプロンプトバージョンを使用する組のみが許可されます。

### Why ?

#### Only 0-shot results are employed for the leaderboard / リーダーボードには0-shotの結果のみを使用します

Recently, many leaderboards have employed 0-shot results for evaluation. We also follow this trend. On the other hand, for some private evaluation of models that support longer prompts, n-shots (n >> 5) evaluation is still used. However, checking the results of huge patterns of n-shots is not practical because it requires a lot of computational resources. Moreover, testing many n-shot results could be p-hacking (It means that there is a good chance of finding extremely high results accidentally). Therefore, we decided to use only 0-shot results for the leaderboard.

最近、多くのリーダーボードが評価に0-shotの結果を使用しているため、この傾向に従うことにしました。一方、より長いプロンプトをサポートするモデルのプライベート評価では、n-shot（n >> 5）の評価がまだ使用されています。ただし、n-shotの多くのパターンの結果を確認することは計算リソースの観点から現実的ではありません。また、多くのn-shotの結果をテストすることはp値hackingになる可能性があります（これは、偶然に非常に高い結果を見つける可能性が高いことを意味します）。そのため、リーダーボードには0-shotの結果のみを使用することにしました。

#### We reject the different prompt selection for each task / 各タスクごとに異なるプロンプトを利用することを禁じます

In the previous version, we allowed different prompt selections for each task. However, this setting is not fair because the prompt selection should not be optimized for each task, and it should be unique to the model. Moreover, testing huge patterns of prompt sets for tasks is not practical because it requires a lot of computational resources. In addition, testing many prompt sets could be p-hacking. Therefore, we decided to enforce the same prompt version for all tasks. However, in some tasks, some prompt versions are missing (e.g., chase-1.0-0.1.2). In those cases, the most similar prompt version is enforced (e.g., chabsa-1.0-0.1 is used instead of chabsa-1.0-0.1.2).

以前のバージョンでは、各タスクごとに異なるプロンプトの選択を許可していました。しかし、プロンプトの選択は各タスクごとに最適化されるべきではなく、モデルに固有であるべきです。また、タスクのためのプロンプトセットの多くのパターンをテストすることは計算リソースの観点から現実的ではありません。さらに、多くのプロンプトセットをテストすることはp値hackingになる可能性があります。そのため、すべてのタスクに同じプロンプトバージョンを強制することにしました。ただし、一部のタスクでは、一部のプロンプトバージョンが欠落している場合があります（例：chabsa-1.0-0.1.2など）。そのような場合は、最も類似したプロンプトバージョンが強制されます（例：chabsa-1.0-0.1.2の代わりにchabsa-1.0-0.1が使用されます）。
