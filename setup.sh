echo "*---------------------------+"
echo "|      Setup iksmproxy      |"
echo "+---------------------------+"
echo ""

echo "*----- splatnet2statink -----*"
echo "Enter splatnet2statink directory:"
read splatnet2statink_path
current_path=`cat config.json | grep splatnet2statink | awk '{print $2}' | sed 's/"//g'`
sed "s%$current_path%$splatnet2statink_path%g" config.json > tmp_config.json
mv tmp_config.json config.json
echo "config.json:"
cat config.json
echo ""

echo "*----- modify service files -----*"
iksm_proxy_path=`pwd`
echo "iksmproxy path: "$iksm_proxy_path
echo "splatnet2statink path: "$splatnet2statink_path
echo ""

cd service/

sed "s%^WorkingDirectory.*%WorkingDirectory=$iksm_proxy_path%g" iksmproxy.service > tmp_iksmproxy.service
mv tmp_iksmproxy.service iksmproxy.service
echo "=== iksmproxy.service ==="
cat iksmproxy.service
echo "========================="
echo ""

sed "s%^WorkingDirectory.*%WorkingDirectory=$splatnet2statink_path%g" splatnet2statink.service > tmp_splatnet2statink.service
mv tmp_splatnet2statink.service splatnet2statink.service
echo "=== splatnet2statink.service ==="
cat splatnet2statink.service
echo "================================"

