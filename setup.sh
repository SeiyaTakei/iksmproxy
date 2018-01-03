echo "*----- modify service files -----*" 
tmp_path=`pwd`
iksm_proxy_path=`echo $tmp_path/main.py` 
echo "iksmproxy path: "$iksm_proxy_path
splatnet2statink_path=`cat config.json | grep splatnet2statink | awk '{print $2}' | sed 's/"//g'`
echo "splatnet2statink path: "$splatnet2statink_path
cd service/
sed "s%^WorkingDirectory.*%WorkingDirectory=$iksm_proxy_path%g" iksmproxy.service > tmp_iksmproxy.service
mv tmp_iksmproxy.service iksmproxy.service

sed "s%^WorkingDirectory.*%WorkingDirectory=$splatnet2statink_path%g" splatnet2statink.service > tmp_splatnet2statink.service
mv tmp_splatnet2statink.service splatnet2statink.service
