<!-- included start from bgp/afi-ipv4-ipv6-flowspec.xml.i -->
<tagNode name="flowspec">
  <properties>
    <help>Network in the BGP routing table to display</help>
    <completionHelp>
      <list>&lt;x.x.x.x&gt; &lt;x.x.x.x/x&gt; &lt;h:h:h:h:h:h:h:h&gt; &lt;h:h:h:h:h:h:h:h/x&gt;</list>
    </completionHelp>
  </properties>
  <children>
    #include <include/bgp/prefix-bestpath-multipath.xml.i>
  </children>
  <command>${ngnos_op_scripts_dir}/vtysh_wrapper.sh $@</command>
</tagNode>
<node name="flowspec">
  <properties>
    <help>Flowspec Address Family modifier</help>
  </properties>
  <children>
    #include <include/bgp/afi-common.xml.i>
    #include <include/bgp/afi-ipv4-ipv6-common.xml.i>
    #include <include/vtysh-generic-detail.xml.i>
  </children>
  <command>${ngnos_op_scripts_dir}/vtysh_wrapper.sh $@</command>
</node>
<!-- included end -->
