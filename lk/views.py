from django.shortcuts import render


#{'notification_type': ['p2p-incoming'], Для переводов из кошелька — p2p-incoming. Для переводов с произвольной карты — card-incoming.
#  'bill_id': [''],
#  'amount': ['9.95'], Сумма, которая зачислена на счет получателя.
#  'codepro': ['false'], Для переводов из кошелька — перевод защищен кодом протекции. Для переводов с произвольной карты — всегда false.
#  'withdraw_amount': ['10.00'], Сумма, которая списана со счета отправителя.
#  'unaccepted': ['false'], Перевод еще не зачислен. Получателю нужно освободить место в кошельке или использовать код протекции (если codepro=true).
#  'label': ['o_id:1;p_id:0'], 	Метка платежа. Если ее нет, параметр содержит пустую строку.
#  'datetime': ['2019-10-30T18:01:36Z'],
#  'sender': ['410016706719303'], Для переводов из кошелька — номер счета отправителя. Для переводов с произвольной карты — параметр содержит пустую строку.
#  'sha1_hash': ['a6c6cad73bf00ef918391881663f3de9efcf4f7d'],
#  'operation_label': ['254be3be-0011-5000-a000-14feae3414d0'],
#  'operation_id': ['625773696428228008'],                           Идентификатор операции в истории счета получателя.
#  'currency': ['643']}


#notification_type&operation_id&amount&currency&datetime&sender&codepro&notification_secret&label