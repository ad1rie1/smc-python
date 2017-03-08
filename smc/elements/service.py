"""
Module reprenting service related elements in the SMC
"""
from smc.base.model import Element, ElementCreator

class TCPService(Element):
    """ 
    Represents a TCP based service in SMC
    TCP Service can use a range of ports or single port. If using
    single port, set only min_dst_port. If using range, set both
    min_dst_port and max_dst_port. 
    
    Create a TCP Service for port 5000::
    
        TCPService.create('tcpservice', 5000, comment='my service')
    """
    typeof = 'tcp_service'
    
    def __init__(self, name, meta=None):
        super(TCPService, self).__init__(name, meta)
        pass
        
    @classmethod
    def create(cls, name, min_dst_port, max_dst_port=None,
               comment=None):
        """
        Create the TCP service
        
        :param str name: name of tcp service
        :param int min_dst_port: minimum destination port value
        :param int max_dst_port: maximum destination port value
        :return: str href: href location of new element
        :raises: :py:class:`smc.api.exceptions.CreateElementFailed`
        """
        comment = comment if comment else ''
        max_dst_port = max_dst_port if max_dst_port is not None else ''
        cls.json = {'name': name,
                    'min_dst_port': min_dst_port,
                    'max_dst_port': max_dst_port,
                    'comment': comment}
        
        return ElementCreator(cls)
    
    @property
    def protocol_agent(self):
        """ Protocol Agent for this service
        
        :return: :py:class:`smc.elements.service.Protocol` or None
        """
        href = self.data.get('protocol_agent_ref')
        if href:
            return Element.from_href(href)
    
class UDPService(Element):
    """ 
    UDP Services can use a range of ports or single port. If using
    single port, set only min_dst_port. If using range, set both
    min_dst_port and max_dst_port. 
    
    Create a UDP Service for port range 5000-5005::
    
        UDPService('udpservice', 5000, 5005).create()
    """
    typeof = 'udp_service'
    
    def __init__(self, name, meta=None):
        super(UDPService, self).__init__(name, meta)
        pass
        
    @classmethod
    def create(cls, name, min_dst_port, max_dst_port=None,
               comment=None):
        """
        Create the UDP Service
        
        :param str name: name of udp service
        :param int min_dst_port: minimum destination port value
        :param int max_dst_port: maximum destination port value
        :return: str href: href location of new element
        :raises: :py:class:`smc.api.exceptions.CreateElementFailed`
        """
        comment = comment if comment else ''
        max_dst_port = max_dst_port if max_dst_port is not None else ''
        cls.json = {'name': name,
                    'min_dst_port': min_dst_port,
                    'max_dst_port': max_dst_port,
                    'comment': comment}
        
        return ElementCreator(cls)

class IPService(Element):
    """ 
    Represents an IP-Proto service in SMC
    IP Service is represented by a protocol number. This will display
    in the SMC under Services -> IP-Proto. It may also show up in 
    Services -> With Protocol if the protocol is tied to a Protocol Agent.
    
    Create an IP Service for protocol 93 (AX.25)::
    
        IPService('ipservice', 93).create()
    """
    typeof = 'ip_service'
    
    def __init__(self, name, meta=None):
        super(IPService, self).__init__(name, meta)
        pass
        
    @classmethod
    def create(cls, name, protocol_number, comment=None):
        """
        Create the IP Service
        
        :param str name: name of ip-service
        :param int protocol_number: ip proto number for this service
        :return: str href: href location of new element
        :raises: :py:class:`smc.api.exceptions.CreateElementFailed`
        """
        comment = comment if comment else ''
        cls.json = {'name': name,
                    'protocol_number': protocol_number,
                    'comment': comment}
        
        return ElementCreator(cls)

class EthernetService(Element):
    """ 
    Represents an ethernet based service in SMC
    Ethernet service only supports adding eth2 frame type. 
    Ethertype field should be the ethernet2 ethertype hex code 
    converted into decimal format. 
    
    Create an ethernet rule for DEC DNS which has an ethernet type
    hex code of 803C, and a decimal conversion value of 32828:
    
        EthernetService.create(name='myService', ethertype='32828')
    
    .. note:: Ethernet Services are only available as of SMC version 6.1.2
    
    """
    typeof = 'ethernet_service'
    
    def __init__(self, name, meta=None):
        super(EthernetService, self).__init__(name, meta)
        pass

    @classmethod
    def create(cls, name, frame_type='eth2', ethertype=None, comment=None):
        """
        Create an ethernet service
        
        :param str name: name of service
        :param str frame_type: ethernet frame type, eth2\|llc\|snap
        :param str ethertype: hex string code for protocol
        :param str comment: optional comment
        :return: str href: href location of new element
        :raises: :py:class:`smc.api.exceptions.CreateElementFailed`
        """
        comment = comment if comment else ''
        cls.json = {'frame_type': frame_type,
                    'name': name,
                    'value1': ethertype,
                    'comment': comment}
        
        return ElementCreator(cls)

class Protocol(Element):
    """ 
    Represents a protocol module in SMC 
    Add is not possible 
    """
    typeof = 'protocol'
    
    def __init__(self, name, meta=None):
        super(Protocol, self).__init__(name, meta)
        pass

class ICMPService(Element):
    """ 
    Represents an ICMP Service in SMC
    Use the RFC icmp type and code fields to set values. ICMP
    type is required, icmp code is optional but will make the service
    more specific if type codes exist.
    
    Create an ICMP service using type 3, code 7 (Dest. Unreachable)::
    
        ICMPService.create(name='api-icmp', icmp_type=3, icmp_code=7)
    """
    typeof = 'icmp_service'
    
    def __init__(self, name, meta=None):
        super(ICMPService, self).__init__(name, meta)
        pass
        
    @classmethod
    def create(cls, name, icmp_type, icmp_code=None, comment=None):
        """
        Create the ICMP service element
        
        :param str name: name of service
        :param int icmp_type: icmp type field
        :param int icmp_code: icmp type code
        :return: str href: href location of new element
        :raises: :py:class:`smc.api.exceptions.CreateElementFailed`
        """
        comment = comment if comment else ''
        icmp_code = icmp_code if icmp_code else ''
        cls.json = {'name': name,
                    'icmp_type': icmp_type,
                    'icmp_code': icmp_code,
                    'comment': comment}
        
        return ElementCreator(cls)

class ICMPIPv6Service(Element):
    """ 
    Represents an ICMPv6 Service type in SMC
    Set the icmp type field at minimum. At time of writing the
    icmp code fields were all 0.
    
    Create an ICMPv6 service for Neighbor Advertisement Message::
    
        ICMPIPv6Service.create('api-Neighbor Advertisement Message', 139)
    """
    typeof = 'icmp_ipv6_service'
    
    def __init__(self, name, meta=None):
        super(ICMPIPv6Service, self).__init__(name, meta)
        pass
  
    @classmethod
    def create(cls, name, icmp_type, comment=None):
        """
        Create the ICMPIPv6 service element
        
        :param str name: name of service
        :param int icmp_type: ipv6 icmp type field
        :return: str href: href location of new element
        :raises: :py:class:`smc.api.exceptions.CreateElementFailed`
        """
        comment = comment if comment else ''
        cls.json = {'name': name,
                    'icmp_type': icmp_type,
                    'comment': comment}
        
        return ElementCreator(cls)
    
class ApplicationSituation(Element):
    """
    Application Situations are network applications used as rule service
    parameters in policies. Applications examples are 'facebook chat', 
    'facebook plugins', etc. These transcend the layer 7 protocol being
    used (most commonly port 80 and 443) and instead provide visibility 
    into the application itself.
    """
    typeof = 'application_situation'
    
    def __init__(self, name, meta=None):
        super(ApplicationSituation, self).__init__(name, meta)
        pass
    